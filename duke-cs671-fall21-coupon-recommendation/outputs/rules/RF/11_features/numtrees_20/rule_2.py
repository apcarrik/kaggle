def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[2]>0:
		# {"feature": "Coffeehouse", "instances": 45, "metric_value": 0.8673, "depth": 2}
		if obj[7]>0.0:
			# {"feature": "Age", "instances": 33, "metric_value": 0.7455, "depth": 3}
			if obj[3]<=5:
				# {"feature": "Education", "instances": 27, "metric_value": 0.8256, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Direction_same", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[9]<=0:
						# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[6]>0.0:
							return 'True'
						elif obj[6]<=0.0:
							# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[5]>6:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=2.0:
											return 'False'
										elif obj[8]>2.0:
											return 'True'
										else: return 'True'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								elif obj[5]<=6:
									return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]>0:
						return 'False'
					else: return 'False'
				elif obj[4]>0:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4138, "depth": 5}
					if obj[8]<=2.0:
						return 'True'
					elif obj[8]>2.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]>5:
				return 'True'
			else: return 'True'
		elif obj[7]<=0.0:
			# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=10:
					# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[3]>1:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]>1:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]>0.0:
								return 'True'
							elif obj[6]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]<=1:
						return 'True'
					else: return 'True'
				elif obj[5]>10:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[6]<=2.0:
			return 'False'
		elif obj[6]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
