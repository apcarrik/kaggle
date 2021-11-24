def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 2}
		if obj[3]<=14:
			# {"feature": "Distance", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>1:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[1]<=1:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						return 'False'
					else: return 'False'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[6]>2:
				return 'False'
			else: return 'False'
		elif obj[3]>14:
			return 'True'
		else: return 'True'
	elif obj[2]>2:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[1]>3:
			# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]>7:
					return 'False'
				elif obj[3]<=7:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=3:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>1.0:
				return 'True'
			else: return 'True'
		elif obj[1]<=3:
			return 'False'
		else: return 'False'
	else: return 'False'
