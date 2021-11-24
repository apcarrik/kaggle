def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[2]<=7:
				return 'True'
			elif obj[2]>7:
				return 'False'
			else: return 'False'
		elif obj[1]>1:
			# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[2]>4:
				return 'False'
			elif obj[2]<=4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
