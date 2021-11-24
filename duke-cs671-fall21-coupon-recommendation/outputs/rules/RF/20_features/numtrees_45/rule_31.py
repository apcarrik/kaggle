def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Driving_to", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Bar", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[14]<=2.0:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[12]>1:
					return 'False'
				elif obj[12]<=1:
					# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]>1:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]<=3:
					return 'True'
				elif obj[4]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[14]>2.0:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
