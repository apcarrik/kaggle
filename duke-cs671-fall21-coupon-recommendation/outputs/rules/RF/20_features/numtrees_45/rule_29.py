def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[8]<=5:
		# {"feature": "Passanger", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[14]<=2.0:
				return 'False'
			elif obj[14]>2.0:
				# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>1:
			# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[7]<=0:
				# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[4]>0:
					return 'True'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			elif obj[7]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]>5:
		return 'True'
	else: return 'True'
