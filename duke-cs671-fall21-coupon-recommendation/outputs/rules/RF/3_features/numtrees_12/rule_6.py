def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9555, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 62, "metric_value": 0.8238, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 59, "metric_value": 0.8432, "depth": 3}
			if obj[2]<=15.601774662991769:
				return 'True'
			elif obj[2]>15.601774662991769:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[2]<=12:
			# {"feature": "Education", "instances": 20, "metric_value": 0.7219, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>12:
			return 'True'
		else: return 'True'
	else: return 'False'
