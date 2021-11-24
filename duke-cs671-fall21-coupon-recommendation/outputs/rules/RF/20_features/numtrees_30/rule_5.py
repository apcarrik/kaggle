def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[4]>0:
		# {"feature": "Education", "instances": 26, "metric_value": 1.0, "depth": 2}
		if obj[11]<=3:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 3}
			if obj[5]<=3:
				# {"feature": "Restaurantlessthan20", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[16]>1.0:
					# {"feature": "Occupation", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[12]>4:
						# {"feature": "Income", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[13]>2:
							# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[15]<=2.0:
								return 'True'
							elif obj[15]>2.0:
								return 'False'
							else: return 'False'
						elif obj[13]<=2:
							return 'False'
						else: return 'False'
					elif obj[12]<=4:
						return 'False'
					else: return 'False'
				elif obj[16]<=1.0:
					return 'True'
				else: return 'True'
			elif obj[5]>3:
				# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[14]<=2.0:
					return 'True'
				elif obj[14]>2.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[11]>3:
			return 'True'
		else: return 'True'
	elif obj[4]<=0:
		return 'True'
	else: return 'True'
