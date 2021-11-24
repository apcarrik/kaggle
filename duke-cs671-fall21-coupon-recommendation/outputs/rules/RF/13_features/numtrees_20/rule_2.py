def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Time", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[1]>1:
		# {"feature": "Children", "instances": 26, "metric_value": 0.7793, "depth": 2}
		if obj[5]<=0:
			# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.3373, "depth": 3}
			if obj[9]>0.0:
				return 'True'
			elif obj[9]<=0.0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[5]>0:
			# {"feature": "Age", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[4]>1:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[10]<=2.0:
					return 'False'
				elif obj[10]>2.0:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]>4:
						return 'True'
					elif obj[7]<=4:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Passanger", "instances": 25, "metric_value": 0.9427, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.7919, "depth": 3}
			if obj[7]<=9:
				# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[9]>0.0:
					return 'False'
				elif obj[9]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[7]>9:
				# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[11]>0:
					return 'True'
				elif obj[11]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
