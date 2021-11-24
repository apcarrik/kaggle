def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 44, "metric_value": 0.9985, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Distance", "instances": 32, "metric_value": 0.9887, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9576, "depth": 4}
				if obj[3]<=2.0:
					# {"feature": "Coupon", "instances": 28, "metric_value": 0.9403, "depth": 5}
					if obj[0]<=3:
						return 'True'
					elif obj[0]>3:
						return 'True'
					else: return 'True'
				elif obj[3]>2.0:
					return 'False'
				else: return 'False'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[0]>1:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[3]>1.0:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]<=1.0:
					# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[0]>1:
			return 'True'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]>2:
				return 'True'
			elif obj[1]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
