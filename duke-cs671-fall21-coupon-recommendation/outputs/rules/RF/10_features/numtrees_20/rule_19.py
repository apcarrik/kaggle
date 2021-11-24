def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Education", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.971, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Bar", "instances": 19, "metric_value": 0.998, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Occupation", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[4]>1:
						# {"feature": "Coffeehouse", "instances": 12, "metric_value": 1.0, "depth": 6}
						if obj[6]>1.0:
							# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[0]>0:
									# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[9]>2:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]<=2:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							elif obj[1]>1:
								return 'True'
							else: return 'True'
						elif obj[6]<=1.0:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[5]<=0.0:
					# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=0.0:
						return 'False'
					elif obj[6]>0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]<=0.0:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[9]<=2:
					return 'True'
				elif obj[9]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>3:
			return 'False'
		else: return 'False'
	elif obj[2]>2:
		# {"feature": "Occupation", "instances": 22, "metric_value": 0.684, "depth": 2}
		if obj[4]>5:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]>0:
										return 'True'
									elif obj[8]<=0:
										return 'False'
									else: return 'False'
								elif obj[7]>0.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]>0:
										return 'False'
									elif obj[8]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[6]>1.0:
								return 'True'
							else: return 'True'
						elif obj[3]>2:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[5]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[4]<=5:
			return 'True'
		else: return 'True'
	else: return 'True'
