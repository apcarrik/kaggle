def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[1]>0:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[3]<=16:
			# {"feature": "Passanger", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[0]>0:
				# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.8113, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[6]>1:
						# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[6]<=1:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>2.0:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]>16:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[3]<=7:
			return 'False'
		elif obj[3]>7:
			return 'True'
		else: return 'True'
	else: return 'False'
