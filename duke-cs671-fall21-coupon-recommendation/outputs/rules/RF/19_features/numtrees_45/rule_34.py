def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]>0:
		# {"feature": "Age", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[7]<=4:
			# {"feature": "Coupon", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[4]<=3:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[0]>2:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[11]<=7:
						# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>55:
							# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]<=55:
							return 'True'
						else: return 'True'
					elif obj[11]>7:
						return 'False'
					else: return 'False'
				elif obj[0]<=2:
					return 'True'
				else: return 'True'
			elif obj[4]>3:
				return 'False'
			else: return 'False'
		elif obj[7]>4:
			return 'True'
		else: return 'True'
	elif obj[3]<=0:
		return 'False'
	else: return 'False'
