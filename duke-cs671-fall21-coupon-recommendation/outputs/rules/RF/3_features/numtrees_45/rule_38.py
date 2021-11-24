def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]<=15:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.9183, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[1]<=1:
				return 'True'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]>15:
		return 'False'
	else: return 'False'
