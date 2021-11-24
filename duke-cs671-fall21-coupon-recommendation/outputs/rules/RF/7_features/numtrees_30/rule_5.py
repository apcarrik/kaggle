def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[1]>1:
		# {"feature": "Education", "instances": 24, "metric_value": 0.9544, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 3}
			if obj[3]<=11:
				# {"feature": "Passanger", "instances": 22, "metric_value": 0.9024, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[4]<=0.0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>2:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[6]>1:
						return 'True'
					elif obj[6]<=1:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>11:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[3]>1:
			return 'False'
		elif obj[3]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
