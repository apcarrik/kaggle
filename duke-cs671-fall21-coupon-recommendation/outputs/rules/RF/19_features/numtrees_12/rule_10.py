def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9143, "depth": 1}
	if obj[4]>1:
		# {"feature": "Income", "instances": 60, "metric_value": 0.8113, "depth": 2}
		if obj[12]>2:
			# {"feature": "Temperature", "instances": 40, "metric_value": 0.9341, "depth": 3}
			if obj[2]>30:
				# {"feature": "Occupation", "instances": 32, "metric_value": 0.9887, "depth": 4}
				if obj[11]<=11:
					# {"feature": "Coupon_validity", "instances": 29, "metric_value": 0.9576, "depth": 5}
					if obj[5]>0:
						# {"feature": "Passanger", "instances": 21, "metric_value": 0.9984, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[3]<=1:
								# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[7]<=4:
									return 'False'
								elif obj[7]>4:
									# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1]>0:
										return 'False'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[3]>1:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[7]>2:
								return 'True'
							elif obj[7]<=2:
								# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[9]>0:
									# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[10]>0:
										return 'True'
									elif obj[10]<=0:
										return 'False'
									else: return 'False'
								elif obj[9]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[5]<=0:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								return 'False'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[11]>11:
					return 'False'
				else: return 'False'
			elif obj[2]<=30:
				return 'True'
			else: return 'True'
		elif obj[12]<=2:
			# {"feature": "Time", "instances": 20, "metric_value": 0.2864, "depth": 3}
			if obj[3]<=3:
				return 'True'
			elif obj[3]>3:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[7]<=0:
						return 'True'
					elif obj[7]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]<=1:
		# {"feature": "Maritalstatus", "instances": 25, "metric_value": 0.9988, "depth": 2}
		if obj[8]<=1:
			# {"feature": "Bar", "instances": 20, "metric_value": 0.9341, "depth": 3}
			if obj[13]<=1.0:
				# {"feature": "Time", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[11]<=10:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[11]>10:
						return 'True'
					else: return 'True'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			elif obj[13]>1.0:
				# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[7]<=4:
					return 'True'
				elif obj[7]>4:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
