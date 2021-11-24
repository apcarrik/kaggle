def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.8338, "depth": 1}
	if obj[9]<=2.0:
		# {"feature": "Gender", "instances": 28, "metric_value": 0.6769, "depth": 2}
		if obj[3]<=0:
			# {"feature": "Income", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[8]>2:
				# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[8]<=2:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[7]>6:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=4:
						return 'True'
					elif obj[4]>4:
						return 'False'
					else: return 'False'
				elif obj[7]<=6:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]>0:
			return 'True'
		else: return 'True'
	elif obj[9]>2.0:
		# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 2}
		if obj[11]>1.0:
			return 'False'
		elif obj[11]<=1.0:
			# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[8]<=4:
				return 'True'
			elif obj[8]>4:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
