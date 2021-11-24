def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[19]>1:
		# {"feature": "Passanger", "instances": 31, "metric_value": 0.8691, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Restaurantlessthan20", "instances": 21, "metric_value": 0.5917, "depth": 3}
			if obj[16]>1.0:
				return 'False'
			elif obj[16]<=1.0:
				# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[8]<=4:
					return 'True'
				elif obj[8]>4:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[5]>0:
				# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[8]<=6:
					return 'True'
				elif obj[8]>6:
					return 'False'
				else: return 'False'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[19]<=1:
		# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Education", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[11]>0:
				return 'True'
			elif obj[11]<=0:
				# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[9]<=0:
					return 'True'
				elif obj[9]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[6]<=0:
				return 'False'
			elif obj[6]>0:
				# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=0:
					return 'True'
				elif obj[0]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'True'
