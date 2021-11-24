def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[12]>4:
		# {"feature": "Weather", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[2]<=1:
			# {"feature": "Bar", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[14]<=2.0:
				# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[11]<=2:
					# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[15]<=1.0:
						# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[3]>30:
							return 'True'
						elif obj[3]<=30:
							return 'False'
						else: return 'False'
					elif obj[15]>1.0:
						# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[9]<=2:
							return 'False'
						elif obj[9]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]>2:
					return 'False'
				else: return 'False'
			elif obj[14]>2.0:
				return 'False'
			else: return 'False'
		elif obj[2]>1:
			return 'True'
		else: return 'True'
	elif obj[12]<=4:
		return 'True'
	else: return 'True'
