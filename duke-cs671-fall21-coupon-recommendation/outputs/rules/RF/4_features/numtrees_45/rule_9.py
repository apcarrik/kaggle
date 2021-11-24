def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]<=9:
		# {"feature": "Distance", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[3]>1:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[0]>1:
				# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[0]<=3:
				return 'True'
			elif obj[0]>3:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[2]>9:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[0]>1:
			return 'False'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
