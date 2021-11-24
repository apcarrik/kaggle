def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9719, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 112, "metric_value": 0.9403, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 63, "metric_value": 0.9911, "depth": 3}
			if obj[2]<=8:
				return 'True'
			elif obj[2]>8:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			# {"feature": "Occupation", "instances": 49, "metric_value": 0.8031, "depth": 3}
			if obj[2]<=7:
				return 'True'
			elif obj[2]>7:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[2]<=7:
				return 'False'
			elif obj[2]>7:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
