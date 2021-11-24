def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 2}
		if obj[7]<=17:
			# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9587, "depth": 3}
			if obj[10]<=1.0:
				# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[9]>0.0:
					return 'False'
				elif obj[9]<=0.0:
					# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=0:
							return 'True'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]>1.0:
				# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[6]>0:
					return 'True'
				elif obj[6]<=0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[7]>17:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[2]<=3:
			return 'True'
		elif obj[2]>3:
			# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
