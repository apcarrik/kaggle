def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[8]>3:
		# {"feature": "Education", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[1]>1:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[2]>0:
					# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[9]>0:
						return 'True'
					elif obj[9]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[7]>2:
			# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[11]<=2.0:
				return 'False'
			elif obj[11]>2.0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=3:
					return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[8]<=3:
		return 'True'
	else: return 'True'
