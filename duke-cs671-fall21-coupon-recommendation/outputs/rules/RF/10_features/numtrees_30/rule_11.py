def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[6]<=1.0:
		# {"feature": "Time", "instances": 19, "metric_value": 0.7425, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[4]<=11:
					# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[9]>1:
							return 'False'
						elif obj[9]<=1:
							return 'True'
						else: return 'True'
					elif obj[3]>2:
						return 'True'
					else: return 'True'
				elif obj[4]>11:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[1]>1:
			return 'False'
		else: return 'False'
	elif obj[6]>1.0:
		# {"feature": "Time", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[1]>0:
			# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[8]<=0:
					# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]<=5:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>1:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[9]>1:
									return 'False'
								elif obj[9]<=1:
									return 'True'
								else: return 'True'
							elif obj[2]<=1:
								return 'True'
							else: return 'True'
						elif obj[4]>5:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[8]>0:
					return 'True'
				else: return 'True'
			elif obj[5]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
