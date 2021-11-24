def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Weather", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]<=0:
		# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[3]>0:
			# {"feature": "Occupation", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[11]>2:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[0]>1:
					# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]>30:
							return 'False'
						elif obj[2]<=30:
							return 'True'
						else: return 'True'
					elif obj[6]>0:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[11]<=2:
				return 'True'
			else: return 'True'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	elif obj[1]>0:
		return 'True'
	else: return 'True'
