def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Age", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[4]>0:
			# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Income", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=3:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>1:
							return 'True'
						elif obj[1]<=1:
							return 'False'
						else: return 'False'
					elif obj[8]>3:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=5:
						return 'True'
					elif obj[7]>5:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>2:
				return 'True'
			else: return 'True'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	elif obj[2]>3:
		# {"feature": "Income", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[8]<=6:
			# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[9]<=0.0:
					return 'False'
				elif obj[9]>0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]>6:
			return 'True'
		else: return 'True'
	else: return 'False'
