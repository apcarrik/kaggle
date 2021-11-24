def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[12]<=12:
		# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[18]<=0:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[5]>1:
				# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[11]>0:
					# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]>30:
						return 'False'
					elif obj[3]<=30:
						return 'True'
					else: return 'True'
				elif obj[11]<=0:
					return 'True'
				else: return 'True'
			elif obj[5]<=1:
				return 'False'
			else: return 'False'
		elif obj[18]>0:
			return 'True'
		else: return 'True'
	elif obj[12]>12:
		# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[2]<=0:
			return 'True'
		elif obj[2]>0:
			return 'False'
		else: return 'False'
	else: return 'True'
