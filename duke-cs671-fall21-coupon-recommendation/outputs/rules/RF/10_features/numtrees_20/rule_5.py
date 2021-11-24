def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[2]>0:
		# {"feature": "Coffeehouse", "instances": 45, "metric_value": 0.9389, "depth": 2}
		if obj[6]<=3.0:
			# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.8224, "depth": 3}
			if obj[7]<=1.0:
				# {"feature": "Education", "instances": 28, "metric_value": 0.9059, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Bar", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[4]>2:
							# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[9]<=2:
									return 'True'
								elif obj[9]>2:
									# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]>3:
								return 'False'
							else: return 'False'
						elif obj[4]<=2:
							return 'True'
						else: return 'True'
					elif obj[5]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[3]>0:
					# {"feature": "Bar", "instances": 14, "metric_value": 1.0, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Time", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[4]<=11:
									return 'False'
								elif obj[4]>11:
									return 'True'
								else: return 'True'
							elif obj[1]>3:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>1.0:
				return 'True'
			else: return 'True'
		elif obj[6]>3.0:
			# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[7]>1.0:
				# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[3]<=3:
					return 'False'
				elif obj[3]>3:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						return 'False'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]<=1.0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
