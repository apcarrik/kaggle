def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.874, "depth": 1}
	if obj[13]<=0.0:
		# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.5033, "depth": 2}
		if obj[14]<=3.0:
			# {"feature": "Distance", "instances": 26, "metric_value": 0.3912, "depth": 3}
			if obj[18]>1:
				return 'True'
			elif obj[18]<=1:
				# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[14]>3.0:
			return 'False'
		else: return 'False'
	elif obj[13]>0.0:
		# {"feature": "Coffeehouse", "instances": 24, "metric_value": 1.0, "depth": 2}
		if obj[14]>1.0:
			# {"feature": "Restaurantlessthan20", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[15]<=2.0:
				return 'False'
			elif obj[15]>2.0:
				# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3]<=1:
					# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[12]>0:
						return 'False'
					elif obj[12]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[14]<=1.0:
			# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[7]<=4:
				return 'True'
			elif obj[7]>4:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
