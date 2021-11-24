def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 36, "metric_value": 0.8524, "depth": 2}
		if obj[9]>0.0:
			# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.6632, "depth": 3}
			if obj[10]<=1.0:
				# {"feature": "Age", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Time", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[1]>1:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[7]<=14:
							return 'True'
						elif obj[7]>14:
							return 'False'
						else: return 'False'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]>1.0:
				return 'True'
			else: return 'True'
		elif obj[9]<=0.0:
			# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[3]>0:
				return 'False'
			elif obj[3]<=0:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]>0:
					return 'True'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[8]<=1.0:
			return 'False'
		elif obj[8]>1.0:
			# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[4]>1:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[11]<=0:
						return 'True'
					elif obj[11]>0:
						return 'False'
					else: return 'False'
				elif obj[10]>1.0:
					return 'False'
				else: return 'False'
			elif obj[4]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
