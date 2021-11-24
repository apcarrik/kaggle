def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[9]<=2:
		# {"feature": "Occupation", "instances": 45, "metric_value": 0.9996, "depth": 2}
		if obj[4]<=12:
			# {"feature": "Bar", "instances": 41, "metric_value": 0.9892, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Coupon", "instances": 36, "metric_value": 0.9641, "depth": 4}
				if obj[2]>0:
					# {"feature": "Passanger", "instances": 25, "metric_value": 0.9988, "depth": 5}
					if obj[0]>0:
						# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Time", "instances": 20, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9612, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9799, "depth": 9}
									if obj[6]>0.0:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[6]<=0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]>2.0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[7]>1.0:
										# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6]>1.0:
											return 'False'
										elif obj[6]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[7]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[8]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[3]>2:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[6]>0.0:
						# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[3]<=2:
							return 'False'
						elif obj[3]>2:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>2.0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>12:
			return 'True'
		else: return 'True'
	elif obj[9]>2:
		return 'False'
	else: return 'False'
