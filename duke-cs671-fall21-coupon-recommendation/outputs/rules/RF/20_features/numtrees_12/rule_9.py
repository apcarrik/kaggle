def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[19]<=2:
		# {"feature": "Occupation", "instances": 70, "metric_value": 0.8981, "depth": 2}
		if obj[12]>4:
			# {"feature": "Age", "instances": 49, "metric_value": 0.9633, "depth": 3}
			if obj[8]>1:
				# {"feature": "Income", "instances": 30, "metric_value": 1.0, "depth": 4}
				if obj[13]>1:
					# {"feature": "Bar", "instances": 25, "metric_value": 0.971, "depth": 5}
					if obj[14]<=2.0:
						# {"feature": "Temperature", "instances": 20, "metric_value": 0.8813, "depth": 6}
						if obj[3]>30:
							# {"feature": "Time", "instances": 18, "metric_value": 0.7642, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Restaurantlessthan20", "instances": 12, "metric_value": 0.9183, "depth": 8}
								if obj[16]<=2.0:
									# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[11]>1:
										# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[5]>0:
											return 'False'
										elif obj[5]<=0:
											return 'True'
										else: return 'True'
									elif obj[11]<=1:
										return 'True'
									else: return 'True'
								elif obj[16]>2.0:
									return 'False'
								else: return 'False'
							elif obj[4]>3:
								return 'False'
							else: return 'False'
						elif obj[3]<=30:
							return 'True'
						else: return 'True'
					elif obj[14]>2.0:
						# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[6]>0:
							return 'True'
						elif obj[6]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[13]<=1:
					return 'True'
				else: return 'True'
			elif obj[8]<=1:
				# {"feature": "Coupon", "instances": 19, "metric_value": 0.7425, "depth": 4}
				if obj[5]>1:
					return 'True'
				elif obj[5]<=1:
					# {"feature": "Driving_to", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[12]<=4:
			# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.5917, "depth": 3}
			if obj[15]>1.0:
				return 'True'
			elif obj[15]<=1.0:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Bar", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[14]<=1.0:
						return 'True'
					elif obj[14]>1.0:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[19]>2:
		# {"feature": "Income", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[13]<=6:
			# {"feature": "Education", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[11]<=3:
				return 'False'
			elif obj[11]>3:
				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=0:
					return 'True'
				elif obj[2]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[13]>6:
			return 'True'
		else: return 'True'
	else: return 'False'
