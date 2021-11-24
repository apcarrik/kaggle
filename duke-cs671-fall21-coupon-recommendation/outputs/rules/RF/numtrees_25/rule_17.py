def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Passanger", "instances": 41, "metric_value": 0.9474, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Bar", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[14]<=2.0:
			# {"feature": "Occupation", "instances": 27, "metric_value": 0.9911, "depth": 3}
			if obj[12]>2:
				# {"feature": "Children", "instances": 21, "metric_value": 0.9852, "depth": 4}
				if obj[10]<=0:
					# {"feature": "Income", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[13]<=5:
						# {"feature": "Temperature", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[3]>55:
							return 'False'
						elif obj[3]<=55:
							# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[2]>0:
								return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[13]>5:
						# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[5]>2:
							return 'True'
						elif obj[5]<=2:
							# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[10]>0:
					return 'True'
				else: return 'True'
			elif obj[12]<=2:
				return 'False'
			else: return 'False'
		elif obj[14]>2.0:
			return 'True'
		else: return 'True'
	elif obj[1]>1:
		return 'True'
	else: return 'True'
