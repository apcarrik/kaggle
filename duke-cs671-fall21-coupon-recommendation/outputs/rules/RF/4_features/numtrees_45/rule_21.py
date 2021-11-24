def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[2]>1:
					return 'False'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]>2:
		# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[2]<=10:
				return 'False'
			elif obj[2]>10:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
