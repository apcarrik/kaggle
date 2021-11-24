def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[13]<=1.0:
		# {"feature": "Gender", "instances": 27, "metric_value": 0.9183, "depth": 2}
		if obj[5]>0:
			# {"feature": "Children", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[8]>0:
				# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[12]<=1.0:
					# {"feature": "Income", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[11]<=5:
						return 'False'
					elif obj[11]>5:
						return 'True'
					else: return 'True'
				elif obj[12]>1.0:
					return 'True'
				else: return 'True'
			elif obj[8]<=0:
				return 'False'
			else: return 'False'
		elif obj[5]<=0:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[10]>2:
				# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[4]>0:
					# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[11]<=3:
						return 'True'
					elif obj[11]>3:
						return 'False'
					else: return 'False'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			elif obj[10]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[13]>1.0:
		# {"feature": "Coupon_validity", "instances": 24, "metric_value": 0.7383, "depth": 2}
		if obj[4]>0:
			# {"feature": "Direction_same", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[16]<=0:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]<=1:
						return 'False'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=2:
						return 'True'
					elif obj[7]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[16]>0:
				return 'True'
			else: return 'True'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	else: return 'True'
