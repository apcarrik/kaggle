def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[18]>1:
		# {"feature": "Time", "instances": 27, "metric_value": 0.951, "depth": 2}
		if obj[3]>1:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[11]>1:
				# {"feature": "Weather", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[10]<=2:
						return 'False'
					elif obj[10]>2:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[11]<=1:
				return 'True'
			else: return 'True'
		elif obj[3]<=1:
			# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[8]>0:
				return 'False'
			elif obj[8]<=0:
				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[18]<=1:
		# {"feature": "Income", "instances": 24, "metric_value": 0.8709, "depth": 2}
		if obj[12]>1:
			# {"feature": "Age", "instances": 18, "metric_value": 0.65, "depth": 3}
			if obj[7]>2:
				return 'True'
			elif obj[7]<=2:
				# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5]>0:
						return 'False'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[12]<=1:
			# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[3]>0:
				return 'False'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
