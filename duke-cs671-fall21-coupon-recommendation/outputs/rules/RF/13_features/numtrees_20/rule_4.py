def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[2]>1:
		# {"feature": "Bar", "instances": 37, "metric_value": 0.9868, "depth": 2}
		if obj[8]<=2.0:
			# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.9993, "depth": 3}
			if obj[10]<=1.0:
				# {"feature": "Occupation", "instances": 20, "metric_value": 0.9341, "depth": 4}
				if obj[7]<=7:
					# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[9]<=2.0:
						# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[3]>0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]>0:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[12]>1:
											return 'True'
										elif obj[12]<=1:
											return 'False'
										else: return 'False'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							elif obj[4]>2:
								return 'True'
							else: return 'True'
						elif obj[6]>1:
							return 'False'
						else: return 'False'
					elif obj[9]>2.0:
						return 'True'
					else: return 'True'
				elif obj[7]>7:
					return 'True'
				else: return 'True'
			elif obj[10]>1.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[7]<=6:
					# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[4]>0:
						# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[11]<=0:
							return 'True'
						elif obj[11]>0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]<=0:
						return 'False'
					else: return 'False'
				elif obj[7]>6:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[8]>2.0:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Education", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[6]<=3:
			# {"feature": "Distance", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[12]>1:
				return 'False'
			elif obj[12]<=1:
				# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
