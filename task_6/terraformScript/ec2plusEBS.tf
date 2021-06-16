provider "aws" {
  region  = "ap-south-1"
  profile = "default"
}

# Step 1 -> Creating Instance
resource "aws_instance" "os1" {
  ami           = "ami-010aff33ed5991201"
  instance_type = "t2.micro"
  tags = {
    Name = "EC2 launched using Face Recognition"
  }
}

# Step 2 -> Creating Volume
resource "aws_ebs_volume" "myvol" {
  availability_zone = aws_instance.os1.availability_zone
  size              = 8

  tags = {
    Name = "Volume2"
  }
}

# Step 3 -> Connecting EBS to EC2
resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.myvol.id
  instance_id = aws_instance.os1.id
}

output "volume_id" {
  value = aws_ebs_volume.myvol.id
}

output "instance_id" {
  value = aws_instance.os1.availability_zone
}

output "availability_zone" {
  value = aws_instance.os1.availability_zone
}
