def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Restaurantlessthan20", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[16]<=2.0:
		# {"feature": "Time", "instances": 23, "metric_value": 0.9656, "depth": 2}
		if obj[4]>0:
			# {"feature": "Coupon", "instances": 18, "metric_value": 1.0, "depth": 3}
			if obj[5]>0:
				# {"feature": "Temperature", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[3]>30:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[12]<=14:
						# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[8]<=3:
							return 'False'
						elif obj[8]>3:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=1:
								return 'True'
							elif obj[1]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[12]>14:
						return 'True'
					else: return 'True'
				elif obj[3]<=30:
					return 'True'
				else: return 'True'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[16]>2.0:
		# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[11]<=2:
			return 'True'
		elif obj[11]>2:
			# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[15]>2.0:
				return 'True'
			elif obj[15]<=2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
