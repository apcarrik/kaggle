def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[4]<=1.0:
		# {"feature": "Occupation", "instances": 37, "metric_value": 0.9995, "depth": 2}
		if obj[3]<=17:
			# {"feature": "Distance", "instances": 32, "metric_value": 0.9745, "depth": 3}
			if obj[6]>1:
				# {"feature": "Coupon", "instances": 21, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 20, "metric_value": 0.8813, "depth": 5}
					if obj[2]>1:
						# {"feature": "Passanger", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[0]>1:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[6]<=1:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[1]<=2:
							return 'False'
						elif obj[1]>2:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>17:
			return 'True'
		else: return 'True'
	elif obj[4]>1.0:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[3]<=14:
			return 'True'
		elif obj[3]>14:
			return 'False'
		else: return 'False'
	else: return 'True'
