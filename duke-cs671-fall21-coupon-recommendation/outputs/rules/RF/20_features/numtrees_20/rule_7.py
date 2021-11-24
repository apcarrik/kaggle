def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[11]<=3:
		# {"feature": "Restaurantlessthan20", "instances": 43, "metric_value": 0.9965, "depth": 2}
		if obj[16]<=3.0:
			# {"feature": "Driving_to", "instances": 39, "metric_value": 0.9995, "depth": 3}
			if obj[0]>0:
				# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 4}
				if obj[5]<=3:
					# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[17]<=1.0:
						# {"feature": "Direction_same", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[18]<=0:
							# {"feature": "Coupon_validity", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[6]>0:
								# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[2]<=0:
									# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[12]<=12:
										return 'False'
									elif obj[12]>12:
										return 'True'
									else: return 'True'
								elif obj[2]>0:
									return 'True'
								else: return 'True'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						elif obj[18]>0:
							return 'True'
						else: return 'True'
					elif obj[17]>1.0:
						return 'False'
					else: return 'False'
				elif obj[5]>3:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				# {"feature": "Passanger", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[1]>1:
					# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[4]<=3:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[12]<=10:
							return 'True'
						elif obj[12]>10:
							return 'False'
						else: return 'False'
					elif obj[4]>3:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[16]>3.0:
			return 'False'
		else: return 'False'
	elif obj[11]>3:
		# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=0:
				return 'True'
			elif obj[2]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
