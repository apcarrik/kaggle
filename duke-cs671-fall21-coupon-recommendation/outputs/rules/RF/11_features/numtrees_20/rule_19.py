def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[5]>5:
		# {"feature": "Distance", "instances": 38, "metric_value": 0.992, "depth": 2}
		if obj[10]<=2:
			# {"feature": "Time", "instances": 36, "metric_value": 0.9799, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 31, "metric_value": 0.9992, "depth": 4}
				if obj[2]>1:
					# {"feature": "Age", "instances": 24, "metric_value": 0.9799, "depth": 5}
					if obj[3]>0:
						# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9984, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[6]>0.0:
								# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]<=1.0:
											return 'True'
										elif obj[7]>1.0:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=0.0:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[0]>1:
									# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]>1.0:
										return 'False'
									elif obj[7]<=1.0:
										return 'True'
									else: return 'True'
								elif obj[0]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]>1.0:
							# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[4]>0:
								# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]>1:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]>1.0:
											return 'True'
										elif obj[7]<=1.0:
											return 'False'
										else: return 'False'
									elif obj[0]<=1:
										return 'False'
									else: return 'False'
								elif obj[6]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[0]>2:
						# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[3]<=3:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=1.0:
								return 'False'
							elif obj[8]>1.0:
								return 'True'
							else: return 'True'
						elif obj[3]>3:
							return 'True'
						else: return 'True'
					elif obj[0]<=2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[10]>2:
			return 'False'
		else: return 'False'
	elif obj[5]<=5:
		# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3912, "depth": 2}
		if obj[9]<=0:
			return 'True'
		elif obj[9]>0:
			return 'False'
		else: return 'False'
	else: return 'True'
