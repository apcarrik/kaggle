def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[11]>1:
		# {"feature": "Coffeehouse", "instances": 24, "metric_value": 1.0, "depth": 2}
		if obj[8]>0.0:
			# {"feature": "Bar", "instances": 20, "metric_value": 0.971, "depth": 3}
			if obj[7]<=2.0:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[6]>0:
					# {"feature": "Time", "instances": 14, "metric_value": 0.7496, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[4]>0:
							return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]>3:
						# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]<=0:
					return 'True'
				else: return 'True'
			elif obj[7]>2.0:
				# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=0:
					return 'True'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[11]<=1:
		# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[4]<=2:
			return 'True'
		elif obj[4]>2:
			# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
