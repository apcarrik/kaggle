def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[2]>5:
		# {"feature": "Education", "instances": 23, "metric_value": 0.7554, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[0]>0:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Distance", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			return 'True'
		else: return 'True'
	elif obj[2]<=5:
		# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 2}
		if obj[4]>1:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[0]>1:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		elif obj[4]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
