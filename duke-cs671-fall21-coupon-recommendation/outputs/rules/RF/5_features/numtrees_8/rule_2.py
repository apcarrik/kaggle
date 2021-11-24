def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Distance", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[4]<=2:
		# {"feature": "Coupon", "instances": 115, "metric_value": 0.9908, "depth": 2}
		if obj[0]>1:
			# {"feature": "Restaurant20to50", "instances": 81, "metric_value": 0.951, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Occupation", "instances": 74, "metric_value": 0.9227, "depth": 4}
				if obj[2]<=10:
					# {"feature": "Education", "instances": 51, "metric_value": 0.8479, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[2]>10:
					# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]>2.0:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[2]<=6:
					return 'False'
				elif obj[2]>6:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 34, "metric_value": 0.9597, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 21, "metric_value": 0.7919, "depth": 4}
				if obj[2]>4:
					# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[3]>0.0:
						return 'False'
					elif obj[3]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=4:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[2]>2:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[3]>1.0:
						return 'True'
					elif obj[3]<=1.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=2:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[4]>2:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[2]>1:
			return 'False'
		elif obj[2]<=1:
			# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=2.0:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
