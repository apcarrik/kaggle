def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Education", "instances": 35, "metric_value": 0.8224, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Occupation", "instances": 24, "metric_value": 0.65, "depth": 3}
			if obj[3]<=19:
				# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.5586, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Distance", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[5]>1:
						# {"feature": "Passanger", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=2:
							return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			elif obj[3]>19:
				return 'False'
			else: return 'False'
		elif obj[2]>2:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[3]>1:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=1:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'False'
					else: return 'False'
				elif obj[5]>1:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]>3:
		# {"feature": "Passanger", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[2]<=3:
				return 'False'
			elif obj[2]>3:
				# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[5]>1:
					return 'True'
				elif obj[5]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[4]<=1.0:
				return 'True'
			elif obj[4]>1.0:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[5]<=1:
					return 'True'
				elif obj[5]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	else: return 'False'
