def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[0]>2:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[2]<=9:
			# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>9:
			return 'True'
		else: return 'True'
	elif obj[0]<=2:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[2]>6:
			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		elif obj[2]<=6:
			# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
