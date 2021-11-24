def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.8479, "depth": 1}
	if obj[3]>0:
		# {"feature": "Restaurantlessthan20", "instances": 43, "metric_value": 0.7401, "depth": 2}
		if obj[14]>1.0:
			# {"feature": "Maritalstatus", "instances": 34, "metric_value": 0.6024, "depth": 3}
			if obj[7]<=1:
				# {"feature": "Age", "instances": 27, "metric_value": 0.3809, "depth": 4}
				if obj[6]<=4:
					return 'True'
				elif obj[6]>4:
					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[16]<=0:
						return 'True'
					elif obj[16]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>1:
				# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[2]>1:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=3:
						return 'False'
					elif obj[6]>3:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[14]<=1.0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[10]>4:
				# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[10]<=4:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=0:
		# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.9544, "depth": 2}
		if obj[7]>0:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[7]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
