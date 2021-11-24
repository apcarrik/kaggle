def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Income", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[11]<=6:
		# {"feature": "Occupation", "instances": 46, "metric_value": 0.9321, "depth": 2}
		if obj[10]<=7:
			# {"feature": "Weather", "instances": 30, "metric_value": 0.9968, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Coupon", "instances": 27, "metric_value": 0.9751, "depth": 4}
				if obj[3]>0:
					# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.9986, "depth": 5}
					if obj[7]>0:
						# {"feature": "Age", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[6]<=6:
							# {"feature": "Time", "instances": 12, "metric_value": 0.8113, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[12]>-1.0:
									return 'True'
								elif obj[12]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[2]>3:
								# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[6]>6:
							return 'False'
						else: return 'False'
					elif obj[7]<=0:
						# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[2]<=1:
							return 'False'
						elif obj[2]>1:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[10]>7:
			# {"feature": "Age", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[6]<=2:
				return 'False'
			elif obj[6]>2:
				# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[8]<=0:
					return 'False'
				elif obj[8]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[11]>6:
		return 'True'
	else: return 'True'
