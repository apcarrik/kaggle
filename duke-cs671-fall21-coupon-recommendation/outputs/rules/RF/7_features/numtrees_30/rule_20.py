def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[3]<=11:
		# {"feature": "Passanger", "instances": 25, "metric_value": 0.971, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 1.0, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Coupon", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=0:
						return 'False'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>1.0:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]>11:
		# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[1]>2:
			return 'False'
		elif obj[1]<=2:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
