def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[5]>1:
		# {"feature": "Time", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Weather", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[11]<=2:
						return 'False'
					elif obj[11]>2:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[8]<=4:
						return 'True'
					elif obj[8]>4:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>0:
				return 'True'
			else: return 'True'
		elif obj[4]>2:
			return 'True'
		else: return 'True'
	elif obj[5]<=1:
		return 'False'
	else: return 'False'
