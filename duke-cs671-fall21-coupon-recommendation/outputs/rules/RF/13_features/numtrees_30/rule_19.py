def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[7]<=19:
		# {"feature": "Bar", "instances": 32, "metric_value": 0.8571, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Gender", "instances": 22, "metric_value": 0.9457, "depth": 3}
			if obj[3]>0:
				# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[1]>1:
					# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4]<=4:
						return 'False'
					elif obj[4]>4:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=4:
						return 'True'
					elif obj[4]>4:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=0:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=3:
							return 'False'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[8]>1.0:
			# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[9]<=3.0:
				return 'True'
			elif obj[9]>3.0:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[7]>19:
		return 'False'
	else: return 'False'
