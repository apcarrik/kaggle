def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]>5:
		# {"feature": "Education", "instances": 21, "metric_value": 0.8631, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]>1.0:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=1:
						return 'True'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[3]>1.0:
					return 'False'
				elif obj[3]<=1.0:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[2]<=5:
		# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[0]>3:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]>1.0:
					return 'False'
				else: return 'False'
			elif obj[0]<=3:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]<=1.0:
				return 'False'
			elif obj[3]>1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
