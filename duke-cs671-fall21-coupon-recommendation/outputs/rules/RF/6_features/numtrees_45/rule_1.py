def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Education", "instances": 14, "metric_value": 1.0, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[3]>7:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]>1:
						# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]<=7:
					return 'False'
				else: return 'False'
			elif obj[4]>1.0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=14:
					return 'True'
				elif obj[3]>14:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[4]<=1.0:
			return 'True'
		elif obj[4]>1.0:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]>2:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=2:
					return 'False'
				elif obj[2]>2:
					return 'True'
				else: return 'True'
			elif obj[1]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
