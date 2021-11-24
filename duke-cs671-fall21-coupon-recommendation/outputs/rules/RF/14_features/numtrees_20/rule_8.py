def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[7]<=10:
		# {"feature": "Coupon", "instances": 38, "metric_value": 0.9495, "depth": 2}
		if obj[2]>1:
			# {"feature": "Bar", "instances": 31, "metric_value": 0.8238, "depth": 3}
			if obj[9]<=1.0:
				# {"feature": "Age", "instances": 23, "metric_value": 0.6666, "depth": 4}
				if obj[4]>1:
					# {"feature": "Time", "instances": 16, "metric_value": 0.3373, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]<=1:
					# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[8]<=5:
						# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[6]>0:
							return 'False'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[8]>5:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[9]>1.0:
				# {"feature": "Time", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=4:
						return 'True'
					elif obj[4]>4:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[10]>0.0:
				return 'False'
			elif obj[10]<=0.0:
				# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[7]>10:
		# {"feature": "Education", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[6]>0:
			return 'False'
		elif obj[6]<=0:
			# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4]>1:
					return 'False'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'False'
